import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "distilbert-base-uncased", num_labels=3
        )
        self.id2label = {0: "negative", 1: "neutral", 2: "positive"}

    @torch.no_grad()
    def predict(self, texts: List[str]) -> List[Dict[str, float]]:
        try:
            inputs = self.tokenizer(
                texts,
                padding=True,
                truncation=True,
                max_length=512,
                return_tensors="pt",
            )

            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)

            results = []
            for prob in probs:
                sentiment_scores = {
                    self.id2label[i]: float(score) for i, score in enumerate(prob)
                }
                results.append(sentiment_scores)

            return results

        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise RuntimeError(f"Failed to process text: {str(e)}")
