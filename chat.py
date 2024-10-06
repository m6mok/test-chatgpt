from typing import List

from gigachat import GigaChat

from chat_types import AssistantMessage, SystemMessage, UserMessage


class ContentError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Client(GigaChat):
    def __init__(
        self,
        history_max_depth: int = 100,
        system_role_promt: str | None = None
    ) -> None:
        if history_max_depth <= 1:
            raise ValueError("history_max_depth must be greater than 1")

        super().__init__(verify_ssl_certs=False)

        self.history_max_depth = history_max_depth
        self.history: List[AssistantMessage | SystemMessage | UserMessage] = []

        if system_role_promt is not None:
            self.add_to_history(SystemMessage(content=system_role_promt))

    def add_to_history(self, message: AssistantMessage | SystemMessage | UserMessage) -> None:
        if len(self.history) >= self.history_max_depth:
            self.history = self.history[1:]
        self.history.append(message)

    def send(
        self,
        promt: str,
        model: str = "GigaChat",
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> str:
        self.add_to_history(UserMessage(content=promt))
        completion = self.chat({
            "messages": self.history,
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature
        })
        if len(completion.choices) == 0:
            raise ContentError("no completion choices")

        response = completion.choices[0].message.content

        self.add_to_history(AssistantMessage(content=response))

        return response
