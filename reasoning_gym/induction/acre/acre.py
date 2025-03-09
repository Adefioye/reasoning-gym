"""ACRE(Abstract Causal REasoning Beyond Covariation) dataset"""

# Culled and Adapted from https://github.com/WellyZhang/ACRE

from dataclasses import dataclass
from random import Random
from typing import Any, Dict, List, Optional

from reasoning_gym.factory import ProceduralDataset, register_dataset

from .blicket import config_control, dist_control, final_parse, serialize
from .const import ALL_CONFIG_SIZE, ATTR_CONFIG_SIZE


# Create blicket questions based on 3 regimes (IID, Comp, Sys)
@dataclass
class ACREDatasetConfig:
    """Configuration for ACRE dataset generation"""

    train: int = 1  # The default is 1 for training, otherwise 0 for validation and testing
    size: int = 500  # Size must be in multiples of 10, Split ratio = 6 : 2 : 2 -> IID : Comp : Sys
    seed: Optional[int] = None

    def validate(self) -> None:
        """Validate configuration parameters"""
        assert self.train in set([0, 1]), "train must be either 0 or 1"
        assert self.size % 10 == 0, "size must be a multiple of 10"


class ACREDataset(ProceduralDataset):

    def __init__(self, config: ACREDatasetConfig):
        super().__init__(config, config.seed, config.size)
        self._questions: List[Dict[str, Any]] = None  # initially None, lazy loading
        self.prompt_template = """You are an expert at inductive reasoning. Generate an output corresponding to the given input. Each example is an input-output pair. The input is a list of objects. Each object in the input list has the format, [color, material, shape].
The presence of certain objects will trigger the light to turn on. The output is either "on", "off", or "undetermined", indicating the state of the light or if the state of the light cannot be determined.
Examples:
{examples}

Input: {input}
Output:
"""

    @property
    def questions(self) -> List[dict[str, Any]]:
        """Lazy load generators only when first accessed"""
        if self._questions is None:
            self._questions = self._load_questions()
        return self._questions

    def _load_questions(self):
        """
        Generates questions of particular size
        """

        iid_size = int(0.6 * self.config.size)
        comp_size = int(0.2 * self.config.size)
        sys_size = int(0.2 * self.config.size)
        rng = Random(self.seed)
        iid_questions = config_control(iid_size, self.config.train, ALL_CONFIG_SIZE, "IID", rng)
        comp_questions = config_control(comp_size, self.config.train, ATTR_CONFIG_SIZE, "Comp", rng)
        sys_questions = dist_control(sys_size, self.config.train, "Sys", rng)

        questions = []
        questions.extend(iid_questions)
        questions.extend(comp_questions)
        questions.extend(sys_questions)
        final_questions = final_parse(serialized_questions=serialize(questions))
        return final_questions

    def __getitem__(self, idx: int) -> dict:
        """Generate a single induction-based list function dataset"""
        inputs = self.questions
        input = inputs[idx]
        examples = input["examples"]
        formatted_examples = ""
        for index, object in enumerate(examples):
            input_ = object["input"]
            output = object["output"]
            formatted_examples += f"""Input {index + 1}: {input_}
Output {index + 1}: {output}
"""
        prompt_input = input["question"]["input"]
        answer = input["question"]["output"]
        question = self.prompt_template.format(examples=formatted_examples, input=prompt_input)
        return {"question": question, "answer": answer, "metadata": {}}


register_dataset("acre", ACREDataset, ACREDatasetConfig)
