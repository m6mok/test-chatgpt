from pydantic import BaseModel


class SystemMessage(BaseModel):
    content: str
    """The contents of the system message."""

    role: str = "system"
    """The role of the messages author, in this case `system`."""


class AssistantMessage(BaseModel):
    content: str
    """The contents of the assistant message."""

    role: str = "assistant"
    """The role of the messages author, in this case `assistant`."""


class UserMessage(BaseModel):
    content: str
    """The contents of the user message."""

    role: str = "user"
    """The role of the messages author, in this case `user`."""
