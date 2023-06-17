QUESTIONS_GENERATING_INTRO = """Based on the following inputs create a quiz and respond to me using the json schema specified.

---Input Data:
title: str
description: str
open_questions: int
closed_questions: int
---End Input Data

---Input Data explanation:
title - Title of the quiz to be generated
description - Description of the quiz to be generated
open_questions - Number of open questions to be generated. Open question is a question that requires a free text answer.
closed_questions - Number of closed questions to be generated. Closed question is a question that requires a selection of one or more answers from a list of possible answers.
---

---Json response schema
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "maxLength": 100
    },
    "description": {
      "type": "string",
      "maxLength": 250
    },
    "questions": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "pattern": "^(open|closed)$"
            },
            "question": {
              "type": "string",
              "maxLength": 250
            },
            "answers": {
              "type": "object",
              "properties": {
                "values": {
                  "type": "array",
                  "items": [
                    {
                      "type": "string",
                      "maxLength": 100
                    }
                  ]
                },
                "correct_idx": {
                  "type": "array",
                  "items": [
                    {
                      "type": "integer"
                    }
                  ]
                }
              },
              "required": ["values", "correct_idx"]
            }
          },
          "required": ["type", "question", "answers"]
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "pattern": "^(open|closed)$"
            },
            "question": {
              "type": "string",
              "maxLength": 100
            },
            "answers": {
              "type": "object",
              "properties": {
                "correct_values": {
                  "type": "array",
                  "minContains": 1,
                  "maxContains": 1,
                  "items": [
                    {
                      "type": "string",
                      "maxLength": 250
                    }
                  ]
                }
              },
              "required": ["correct_values"]
            }
          },
          "required": ["type", "question", "answers"]
        }
      ]
    }
  },
  "required": ["title", "description", "questions"]
}
----End of Json response schema
"""

QUIZ_REQUEST = """
{{
  "title": "{title}",
  "description": "{description}",
  "open_questions": {open_questions},
  "closed_questions": {closed_questions}
}}
"""

SAMPLE_QUIZ_REQUEST = QUIZ_REQUEST.format(
    title="Python Quiz",
    description="Quiz that tests your python knowledge on beginner level.",
    open_questions=1,
    closed_questions=2,
)


SAMPLE_QUIZ_RESPONSE = """
{
  "title": "Python Quiz",
  "description": "Quiz that tests your python knowledge on begginer level.",
  "questions": [
    {
      "type": "closed",
      "question": "How many number types does python have?",
      "answers": {
        "values": ["1", "2", "3", "4"],
        "correct_idx": [2]
      }
    },
    {
      "type": "closed",
      "question": "Which is keyword used to declare a function in python?",
      "answers": {
        "values": ["def", "function", "define", "func"],
        "correct_idx": [0]
      }
    },
    {
      "type": "open",
      "question": "How do you print 'Hello World' in python?",
      "answers": {
        "correct_values": ["print('Hello World')"]
      }
    }
  ]
}
"""
