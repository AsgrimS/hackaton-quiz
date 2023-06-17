# Collections of prompts for GPT

## Quiz generation

```
Based on the following inputs create a quiz and respond to me using the json schema specified.

---Input Data:
quiz_title: "{quiz_title}"
quiz_description: "{quiz_description}"
number_of_questions: "{number_of_questions}"
number_of_open_questions: "{number_of_open_questions}"
number_of_closed_questions: "{number_of_closed_questions}"
---End Input Data

---Json schema
{
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
            "title": {
              "type": "string",
              "maxLength": 100
            },
            "description": {
              "type": "string",
              "maxLength": 250
            },
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
          "required": ["title", "description", "type", "question", "answers"]
        },
        {
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
          "required": ["title", "description", "type", "question", "answers"]
        }
      ]
    }
  },
  "required": ["title", "description", "questions"]
}
----End of Json schema

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
--- enf of example


```
