from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionValidarSabor(Action):
    """Valida se o sabor é feito pela pizzaria"""

    def name(self) -> Text:
        return "action_validar_sabor"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        sabor = tracker.get_slot("sabor")

        sabores_disponiveis = [
            "portuguesa",
            "calabresa",
            "frango",
            "mussarela",
            "margherita",
            "picanha",
        ]

        if sabor and sabor.lower() in sabores_disponiveis:
            dispatcher.utter_message(
                text=f"Boa escolha! Pizza de {sabor} é nossa especialidade."
            )
            return []
        else:
            dispatcher.utter_message(
                text=f"Não temos pizza de {sabor}, escolha outro sabor."
            )
            return [SlotSet("sabor", None)]


class ActionValidarTamanho(Action):
    """Validar se o tamanho existe"""

    def name(self) -> Text:
        return "action_validar_tamanho"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        tamanho = tracker.get_slot("tamanho")

        # Aceita com e sem acento
        tamanhos_disponiveis = ["pequena", "média", "media", "grande"]

        if tamanho and tamanho.lower() in tamanhos_disponiveis:
            dispatcher.utter_message(text=f"Beleza! Tamanho {tamanho} anotado.")
            return []
        else:
            dispatcher.utter_message(
                text=f"Não temos o tamanho '{tamanho}'. Escolha entre pequena, média ou grande."
            )
            return [SlotSet("tamanho", None)]


class ActionSimularEntrega(Action):
    """Simula tempo de entrega"""

    def name(self) -> Text:
        return "action_simular_entrega"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        tamanho = (tracker.get_slot("tamanho") or "").lower()

        if tamanho == "grande":
            tempo = random.randint(35, 50)
        elif tamanho in ("média", "media"):
            tempo = random.randint(25, 40)
        else:
            # pequena ou não informado
            tempo = random.randint(20, 30)

        dispatcher.utter_message(
            text=f"Sua pizza deve chegar em aproximadamente {tempo} minutos! 🍕"
        )
        return []
