import json

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
                "correct": {
                  "type": "array",
                  "items": [
                    {
                      "type": "boolean"
                    }
                  ]
                }
              },
              "required": [
                "values",
                "correct"
              ]
            }
          },
          "required": [
            "type",
            "question",
            "answers"
          ]
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
        "correct": [false, false, true, false]
      }
    },
    {
      "type": "closed",
      "question": "Which of the types below represent the numbers in python?",
      "answers": {
        "values": ["Decimal", "int", "str", "NoneType"],
        "correct": [true, true, false, false]
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


VALIDATE_REQUEST_INTRO = """
Based on the following inputs check correctness level of user_answer against the correct answer.
The correctness level should determined by the similarity of the user_answer and the true_answer. The similarity should be determined by logical similarity of the two answers. The similarity should be determined by the following rules:
- If the user_response is exactly the same as one of the valid_responses the correctness level should be 100
- If the user_response is not exactly the same as one of the valid_responses but is logically the same the correctness level should be 100
- If the user_response is not logically the same as any of the valid_responses the correctness level should be 0
- It is possible to have correctness level between 0 and 100 with two decimal places

Answer in json using the json response schema.

---Input Data:
question: str
valid_responses: ["Memory Safety"]
user_response: "Safe memory"
---End Input Data

---Input Data explanation:
question - Question that the user is answering
true_answer - Correct answer to the question
user_answer - User answer to the question
---End Input Data explanation

---Json response schema
{
"$schema": "http://json-schema.org/draft-04/schema#",
"type": "object",
"properties": {
"question": {
"type": "string"
},
"true_answer": {
"type": "string"
},
"user_answer": {
"type": "string"
},
"correctness_level": {
"type": "number"
}
},
"required": ["question", "true_answer", "user_answer", "correctness_level"]
}
----End of Json response schema
"""


SAMPLE_VALIDATE_REQUEST = json.dumps(
    dict(
        question="How do you print 'Hello World' in python?",
        valid_responses=["print('Hello World')"],
        user_response="use print('Hello World')",
    )
)


SAMPLE_VALIDATE_RESPONSE = """100"""
