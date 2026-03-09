# Firestore Database Schema

## Collections

---

### `users/{userId}`
| Field | Type | Description |
|---|---|---|
| `uid` | string | Firebase Auth UID (matches document ID) |
| `email` | string | User email |
| `displayName` | string | Display name |
| `role` | string | `examinee` \| `admin` |
| `createdAt` | timestamp | Account creation date |
| `preferences` | map | UI preferences (theme, language, etc.) |

---

### `exams/{examId}`
| Field | Type | Description |
|---|---|---|
| `title` | string | Exam title |
| `category` | string | Subject/category tag |
| `description` | string | Exam description |
| `questionIds` | array | List of question document IDs |
| `timeLimit` | number | Time limit in minutes |
| `createdAt` | timestamp | Creation date |
| `createdBy` | string | Admin UID |

---

### `questions/{questionId}`
| Field | Type | Description |
|---|---|---|
| `examId` | string | Parent exam document ID |
| `text` | string | Question body |
| `choices` | array | Array of `{ id: string, text: string }` |
| `correctChoiceId` | string | ID of the correct choice |
| `category` | string | Topic tag |
| `difficulty` | string | `easy` \| `medium` \| `hard` |

---

### `results/{resultId}`
| Field | Type | Description |
|---|---|---|
| `userId` | string | Examinee UID |
| `examId` | string | Exam document ID |
| `score` | number | Raw score (correct answers) |
| `percentage` | number | Score as a percentage |
| `answers` | map | `{ questionId: choiceId }` — submitted answers |
| `submittedAt` | timestamp | Submission time |
| `timeTaken` | number | Time taken in seconds |
