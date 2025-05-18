# george_logic.py

def decide_task_response(task_context):
    """
    Given a task context, return a decision: 'affirm', 'delay', or 'reject'
    """

    if "urgent" in task_context or "now" in task_context:
        return "affirm"
    elif "someday" in task_context or "low priority" in task_context:
        return "delay"
    elif "unclear" in task_context or "invalid" in task_context:
        return "reject"
    else:
        return "affirm"  # default to yes