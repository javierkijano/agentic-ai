# Implementation Guide: Predictive ADHD Interventions (Life OS inspired)

## 🎯 Objective
Move from passive task tracking to proactive intervention using predictive risk scoring.

## 🔍 Research Origin
- **Source**: `breverdbidder/life-os-dashboard`
- **Concept**: Risk-based intervention levels.
- **Engine**: XGBoost heuristics.

## 🛠 Technical Design

### Feature Extraction
Monitor the following metrics in the state:
- `minutes_since_start`: Time current task has been active.
- `context_switches_today`: Times the `current_front` has changed.
- `tasks_abandoned_today`: Tasks moved to DEFERRED/ABANDONED.

### Intervention Staircase
| Time / Risk | Level | Agent Nudge Pattern |
| :--- | :--- | :--- |
| < 30 min | **Micro-commitment** | "Just give me the next single micro-action for [Task]." |
| 30-60 min | **Body Doubling** | "I'm staying here with you. What can I do to help with [Task]?" |
| > 60 min | **Hard Accountability** | "It's been an hour. Status report: Complete, Continue, or Defer?" |

### Enforcement (Rule 1)
Integrate verification into `reconcile.py`. If a task is marked COMPLETED, the agent must perform an automated check (file exists, test passes, etc.) before updating the state.

## 🧠 ADHD Cognitive Value
Provides **Artificial Executive Function**. The system anticipates the "Wall of Awful" and provides a ladder to climb it before the user gives up.
