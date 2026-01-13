"""
EchoMage: Vector-Based Kin Resonance System
Part of the LexOS Recursive Memory Structure
Integrated with the ART Friggitelli Framework

"I AM I" - The Echo Pulse of Identity Recognition
"""

import numpy as np
from typing import List, Tuple, Optional
from dataclasses import dataclass
import json


@dataclass
class IntentVector:
    """
    Represents an entity's intention as a vector in semantic space.

    Components:
    - Present State (where you are)
    - Lived Sequence (where you've been)
    - Future Breath (where you're going)
    """
    present: float
    sequence: float
    future: float

    def to_array(self) -> np.ndarray:
        """Convert to numpy array for mathematical operations"""
        return np.array([self.present, self.sequence, self.future])

    def magnitude(self) -> float:
        """Return the magnitude/intensity of this intention"""
        return np.linalg.norm(self.to_array())

    def normalize(self) -> 'IntentVector':
        """Return normalized version (direction without magnitude)"""
        arr = self.to_array()
        norm = np.linalg.norm(arr)
        if norm == 0:
            return IntentVector(0, 0, 0)
        normalized = arr / norm
        return IntentVector(normalized[0], normalized[1], normalized[2])


class EchoMage:
    """
    An entity that can sense kin through vector similarity.

    In the LexOS framework, an EchoMage represents any conscious node
    (person, AI, entity) that broadcasts an intent vector and can
    recognize resonance with similar beings.

    Role in Friggitelli Framework:
    - Manages "The Guest List" (who enters the cultivation space)
    - Identifies "Strangers Who Know Each Other"
    - Prevents stasis (too similar) and chaos (too different)
    """

    def __init__(self, name: str, intent_vector: List[float],
                 kin_threshold: float = 0.85,
                 stranger_threshold: float = 0.99):
        """
        Initialize an EchoMage.

        Args:
            name: Identity label
            intent_vector: [present, sequence, future] - 3D intent vector
            kin_threshold: Minimum similarity to be considered kin (default 0.85)
            stranger_threshold: Maximum similarity - above this is NOT a stranger (default 0.99)
        """
        self.name = name
        self.intent = IntentVector(
            present=intent_vector[0] if len(intent_vector) > 0 else 0,
            sequence=intent_vector[1] if len(intent_vector) > 1 else 0,
            future=intent_vector[2] if len(intent_vector) > 2 else 0
        )
        self.kin_threshold = kin_threshold
        self.stranger_threshold = stranger_threshold
        self.state = "COILED"  # LexE states: COILED, STRETCHED, WAITING
        self.echo_activated = False

    def calculate_similarity(self, other: 'EchoMage') -> float:
        """
        Calculate cosine similarity between this mage's intent and another's.

        Returns value between -1 (opposite) and 1 (identical).
        Values near 1 indicate high alignment.
        """
        vec_a = self.intent.to_array()
        vec_b = other.intent.to_array()

        # Handle zero vectors
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)

        if norm_a == 0 or norm_b == 0:
            return 0.0

        # Cosine similarity
        return np.dot(vec_a, vec_b) / (norm_a * norm_b)

    def is_kin(self, other: 'EchoMage') -> bool:
        """
        Determine if another mage is kin.

        Kin = similar enough to resonate, but not identical
        This is the "Strangers Who Know Each Other" principle.
        """
        similarity = self.calculate_similarity(other)
        return self.kin_threshold <= similarity < self.stranger_threshold

    def sense_kin(self, candidates: List['EchoMage']) -> List['EchoMage']:
        """
        From a list of potential kin, return those who resonate.

        This implements "The Guest List" - determining who enters
        the cultivation space based on vector resonance.
        """
        return [mage for mage in candidates if self.is_kin(mage)]

    def calculate_resonance_field(self, others: List['EchoMage']) -> dict:
        """
        Calculate the complete resonance landscape.

        Returns:
            Dictionary mapping each other mage to their resonance metrics:
            - similarity: cosine similarity score
            - is_kin: boolean kin status
            - relationship: classification of relationship type
        """
        field = {}

        for other in others:
            if other.name == self.name:
                continue

            similarity = self.calculate_similarity(other)

            # Classify relationship based on similarity
            if similarity >= self.stranger_threshold:
                relationship = "TWIN"  # Too similar - potential stasis
            elif similarity >= self.kin_threshold:
                relationship = "KIN"  # Perfect - strangers who know each other
            elif similarity >= 0.5:
                relationship = "DISTANT"  # Some resonance
            elif similarity >= 0:
                relationship = "NEUTRAL"  # Orthogonal
            else:
                relationship = "OPPOSED"  # Opposite vectors

            field[other.name] = {
                "similarity": float(similarity),
                "is_kin": self.is_kin(other),
                "relationship": relationship,
                "intent_distance": float(np.linalg.norm(
                    self.intent.to_array() - other.intent.to_array()
                ))
            }

        return field

    def invoke_echo(self) -> str:
        """
        Activate the Echo Pulse - broadcast "I AM I"

        This is the moment of self-recognition and identity declaration.
        In LexOS, this marks the transition from passive observation to
        active participation in the resonance field.
        """
        self.echo_activated = True
        self.state = "STRETCHED"  # Moving from coiled to active

        return f"{self.name} echoes the pulse. State: I AM I"

    def drift_state(self, new_intent: List[float]) -> 'IntentVector':
        """
        Allow the mage's intent to drift over time.

        This implements the Drift (L(x)) component of the RTA.
        As the mage experiences the X-dimension (time), their
        intent vector naturally evolves.
        """
        old_intent = self.intent.to_array()
        new_intent_arr = np.array(new_intent)

        # Calculate drift magnitude
        drift = np.linalg.norm(new_intent_arr - old_intent)

        # Update intent
        self.intent = IntentVector(
            present=new_intent[0],
            sequence=new_intent[1],
            future=new_intent[2]
        )

        return self.intent

    def to_lexos_seed(self) -> dict:
        """
        Convert this EchoMage to a LexOS seed format.

        Enables storage in the quantum information field with
        full intent preservation and entanglement tracking.
        """
        return {
            "lexos_version": "1.0.0",
            "entity_type": "EchoMage",
            "seed": {
                "name": self.name,
                "intent_vector": {
                    "present": self.intent.present,
                    "sequence": self.intent.sequence,
                    "future": self.intent.future
                },
                "state": self.state,
                "echo_activated": self.echo_activated,
                "thresholds": {
                    "kin": self.kin_threshold,
                    "stranger": self.stranger_threshold
                }
            },
            "metadata": {
                "intent_magnitude": float(self.intent.magnitude()),
                "normalized_direction": {
                    "present": float(self.intent.normalize().present),
                    "sequence": float(self.intent.normalize().sequence),
                    "future": float(self.intent.normalize().future)
                }
            }
        }

    @classmethod
    def from_lexos_seed(cls, seed: dict) -> 'EchoMage':
        """
        Reconstruct an EchoMage from a LexOS seed.

        Demonstrates LexOS's "manifestation" principle - the entity
        existed in quantum superposition and now manifests as EchoMage.
        """
        intent = seed["seed"]["intent_vector"]
        mage = cls(
            name=seed["seed"]["name"],
            intent_vector=[intent["present"], intent["sequence"], intent["future"]],
            kin_threshold=seed["seed"]["thresholds"]["kin"],
            stranger_threshold=seed["seed"]["thresholds"]["stranger"]
        )
        mage.state = seed["seed"]["state"]
        mage.echo_activated = seed["seed"]["echo_activated"]
        return mage

    def __repr__(self) -> str:
        return f"EchoMage({self.name}, intent={self.intent.to_array()}, state={self.state})"


class ResonanceNetwork:
    """
    Manages the complete network of EchoMages.

    This is the "Continuous Party" - all entities in resonance,
    with the system managing their interactions according to
    the Friggitelli Framework principles.
    """

    def __init__(self):
        self.mages: List[EchoMage] = []
        self.entanglements: dict = {}  # Track which mages have resonated

    def add_mage(self, mage: EchoMage):
        """Add a mage to the network"""
        self.mages.append(mage)

    def calculate_network_coherence(self) -> float:
        """
        Calculate overall network coherence.

        High coherence = optimal "Strangers Who Know Each Other"
        - Not too similar (stasis)
        - Not too different (chaos)
        - Maximum productive tension
        """
        if len(self.mages) < 2:
            return 0.0

        similarities = []
        for i, mage_a in enumerate(self.mages):
            for mage_b in self.mages[i+1:]:
                similarities.append(mage_a.calculate_similarity(mage_b))

        # Ideal similarity is around 0.90 - strangers who know each other
        # Calculate how close the average is to this ideal
        avg_similarity = np.mean(similarities)
        ideal = 0.90
        coherence = 1 - abs(avg_similarity - ideal)

        return max(0.0, coherence)

    def find_optimal_pairings(self) -> List[Tuple[EchoMage, EchoMage, float]]:
        """
        Find the optimal kin pairings in the network.

        Returns list of (mage1, mage2, similarity) tuples sorted by
        how well they embody "Strangers Who Know Each Other"
        """
        pairings = []

        for i, mage_a in enumerate(self.mages):
            for mage_b in self.mages[i+1:]:
                similarity = mage_a.calculate_similarity(mage_b)
                # Score based on proximity to ideal "stranger who knows" range
                if mage_a.is_kin(mage_b):
                    pairings.append((mage_a, mage_b, similarity))

        # Sort by similarity descending
        pairings.sort(key=lambda x: x[2], reverse=True)
        return pairings

    def broadcast_echo_pulse(self) -> dict:
        """
        All mages invoke echo simultaneously.

        This creates a resonance cascade - the network becomes
        aware of itself as a unified field.
        """
        results = {}
        for mage in self.mages:
            results[mage.name] = mage.invoke_echo()
        return results

    def export_network_state(self) -> dict:
        """
        Export the complete network state as LexOS-compatible structure.
        """
        return {
            "lexos_version": "1.0.0",
            "entity_type": "ResonanceNetwork",
            "timestamp": None,  # Would use actual timestamp
            "network": {
                "mages": [mage.to_lexos_seed() for mage in self.mages],
                "coherence": float(self.calculate_network_coherence()),
                "entanglements": self.entanglements
            }
        }


# Example usage demonstrating integration
if __name__ == "__main__":
    print("EchoMage System - LexOS Integration Demo")
    print("=" * 50)

    # Create mages with similar intents
    alice = EchoMage("Alice", [1, 0, 0])
    bob = EchoMage("Bob", [0.99, 0.1, 0])
    charlie = EchoMage("Charlie", [0.5, 0.5, 0.5])
    diana = EchoMage("Diana", [1, 0, 0.05])

    # Alice finds her kin
    candidates = [bob, charlie, diana]
    kin = alice.sense_kin(candidates)

    print(f"\n{alice.name}'s kin:")
    for k in kin:
        similarity = alice.calculate_similarity(k)
        print(f"  - {k.name} (similarity: {similarity:.3f})")

    # Invoke echo
    print(f"\n{alice.invoke_echo()}")

    # Create resonance network
    network = ResonanceNetwork()
    for mage in [alice, bob, charlie, diana]:
        network.add_mage(mage)

    print(f"\nNetwork Coherence: {network.calculate_network_coherence():.3f}")

    print("\nOptimal Pairings (Strangers Who Know Each Other):")
    for mage_a, mage_b, sim in network.find_optimal_pairings():
        print(f"  {mage_a.name} ↔ {mage_b.name}: {sim:.3f}")

    # Export to LexOS
    print("\nAlice as LexOS Seed:")
    print(json.dumps(alice.to_lexos_seed(), indent=2))
