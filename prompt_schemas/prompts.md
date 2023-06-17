# Collections of prompts for GPT

## Quiz generation

```
Based on the following inputs create a quiz and respond to me using the json schema specified.

---Input Data:
quiz_title: ""
quiz_description: ""
number_of_questions: ""
number_of_open_questions: ""
number_of_closed_questions: ""
---End Input Data

---Input Data explanation:
quiz_title - Title of the quiz to be generated
quiz_description - Description of the quiz to be generated
number_of_questions - Total number of questions to be generated. Number of question must be exaclty equal to the sum of number_of_open_questions and number_of_closed_questions
number_of_open_questions - Number of open questions to be generated. Open question is a question that requires a free text answer.
number_of_closed_questions - Number of closed questions to be generated. Closed question is a question that requires a selection of one or more answers from a list of possible answers.
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

---Example json response
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
--- end of example
```

## Open question correctnes

```
``Based on the following inputs check correctness level of user_answer against the correct answer.
The correctness level should determined by the similarity of the user_answer and the true_answer. The similarity should be determined by logical similarity of the two answers. The similarity should be determined by the following rules:
- If the user_answer is exactly the same as the true_answer the correctness level should be 100
- If the user_answer is not exactly the same as the true_answer but is logically the same the correctness level should be 100
- If the user answer is not logically the same as the true_answer the correctness level should be 0
- It is possible to have correctness level between 0 and 100 with two decimal places

Answer in json using the json response schema.

---Input Data:
question: "What is the main advangate of rust programming language?"
true_answer: "Memory Safety"
user_answer: "Safe memory"
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

---Example json response
{
"question": "How do you print 'Hello World' in python?",
"true_answer": "print('Hello World')",
"user_answer": "use print('Hello World')",
"correctness_level": 100
}
--- end of example`
```
