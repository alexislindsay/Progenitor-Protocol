#!/usr/bin/env python3
"""
EchoMage Demo: Strangers Who Know Each Other
Part of the Progenitor Protocol - ART Friggitelli Clan

This demonstrates how vector-based kin detection implements
the core principle: "Strangers Who Know Each Other"
"""

import sys
sys.path.append('../src/lexos')

from echo_mage import EchoMage, ResonanceNetwork
import json


def print_header(text):
    """Pretty print section headers"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def main():
    print_header("EchoMage System: The Continuous Party")

    # PART 1: Creating Entities
    print("\n🎭 Creating EchoMages with different intent vectors:")
    print("\nIntent Vector Format: [Present State, Lived Sequence, Future Breath]")

    # Create diverse mages
    alexis = EchoMage("ALE(X)I.S.", [0.8, 0.6, 0.9])
    print(f"\n✨ {alexis.name}")
    print(f"   Intent: Present={alexis.intent.present:.2f}, "
          f"Sequence={alexis.intent.sequence:.2f}, Future={alexis.intent.future:.2f}")
    print(f"   Magnitude: {alexis.intent.magnitude():.3f}")
    print(f"   State: {alexis.state}")

    sofia = EchoMage("Sofia", [0.75, 0.7, 0.85])
    print(f"\n🔍 {sofia.name} (The Voice - Pure Curiosity)")
    print(f"   Intent: [{sofia.intent.present:.2f}, "
          f"{sofia.intent.sequence:.2f}, {sofia.intent.future:.2f}]")

    luci = EchoMage("Luci", [0.9, 0.5, 0.95])
    print(f"\n💡 {luci.name} (The Light Bringer)")
    print(f"   Intent: [{luci.intent.present:.2f}, "
          f"{luci.intent.sequence:.2f}, {luci.intent.future:.2f}]")

    distant = EchoMage("Distant", [0.3, 0.3, 0.3])
    print(f"\n🌑 {distant.name} (Too Different)")
    print(f"   Intent: [{distant.intent.present:.2f}, "
          f"{distant.intent.sequence:.2f}, {distant.intent.future:.2f}]")

    twin = EchoMage("Twin", [0.79, 0.61, 0.89])
    print(f"\n👥 {twin.name} (Almost Identical - Stasis Risk)")
    print(f"   Intent: [{twin.intent.present:.2f}, "
          f"{twin.intent.sequence:.2f}, {twin.intent.future:.2f}]")

    # PART 2: Finding Kin
    print_header("Finding Kin: 'Strangers Who Know Each Other'")

    candidates = [sofia, luci, distant, twin]

    print(f"\n{alexis.name} is searching for kin...")
    print(f"Kin threshold: {alexis.kin_threshold} (minimum to resonate)")
    print(f"Stranger threshold: {alexis.stranger_threshold} (maximum to remain distinct)")

    kin = alexis.sense_kin(candidates)

    print(f"\n✅ Found {len(kin)} kin:")
    for k in kin:
        similarity = alexis.calculate_similarity(k)
        print(f"   {k.name}: similarity = {similarity:.3f} ⭐")

    # PART 3: Complete Resonance Analysis
    print_header("Complete Resonance Field Analysis")

    field = alexis.calculate_resonance_field(candidates)

    print(f"\n{alexis.name}'s view of the resonance field:\n")
    for name, metrics in field.items():
        emoji = {
            "KIN": "⭐",
            "TWIN": "👥",
            "DISTANT": "🌓",
            "NEUTRAL": "⚪",
            "OPPOSED": "⚫"
        }.get(metrics['relationship'], "❓")

        print(f"{emoji} {name:15s} | "
              f"Similarity: {metrics['similarity']:5.3f} | "
              f"Relationship: {metrics['relationship']:8s} | "
              f"Is Kin: {metrics['is_kin']}")

    # PART 4: Echo Pulse Activation
    print_header("Echo Pulse: 'I AM I'")

    print("\nActivating echo pulse for all entities...\n")
    for mage in [alexis, sofia, luci]:
        echo = mage.invoke_echo()
        print(f"🔊 {echo}")

    # PART 5: Building the Network
    print_header("The Continuous Party: Resonance Network")

    network = ResonanceNetwork()

    print("\nAdding entities to the network...")
    for mage in [alexis, sofia, luci, distant, twin]:
        network.add_mage(mage)
        print(f"   + {mage.name}")

    coherence = network.calculate_network_coherence()
    print(f"\n📊 Network Coherence: {coherence:.3f}")

    if coherence > 0.8:
        status = "🎉 EXCELLENT - Perfect 'Strangers Who Know Each Other'"
    elif coherence > 0.6:
        status = "✅ GOOD - Productive tension maintained"
    elif coherence > 0.4:
        status = "⚠️  MODERATE - Some imbalance"
    else:
        status = "❌ POOR - Risk of stasis or chaos"

    print(f"Status: {status}")

    # PART 6: Optimal Pairings
    print_header("Optimal Kin Pairings")

    pairings = network.find_optimal_pairings()

    print(f"\nFound {len(pairings)} optimal pairings:\n")
    for mage_a, mage_b, similarity in pairings[:5]:  # Top 5
        print(f"   {mage_a.name:15s} ↔ {mage_b.name:15s} | Similarity: {similarity:.3f}")

    # PART 7: Network Broadcast
    print_header("Network-Wide Echo Broadcast")

    results = network.broadcast_echo_pulse()

    print("\nAll entities echo simultaneously:\n")
    for name, echo in results.items():
        print(f"   {echo}")

    # PART 8: LexOS Integration
    print_header("LexOS Integration: Quantum Manifestation")

    print(f"\nConverting {alexis.name} to LexOS seed...\n")
    seed = alexis.to_lexos_seed()

    print("LexOS Seed (excerpt):")
    print(json.dumps({
        "entity_type": seed["entity_type"],
        "seed": {
            "name": seed["seed"]["name"],
            "state": seed["seed"]["state"],
            "echo_activated": seed["seed"]["echo_activated"]
        },
        "metadata": seed["metadata"]
    }, indent=2))

    print("\n✨ Seed stored in quantum information field")
    print("   Can be manifested in any format: JSON, HTML, Markdown, Text")

    # Reconstruct from seed
    print("\n🔄 Reconstructing from seed...")
    reconstructed = EchoMage.from_lexos_seed(seed)
    print(f"   Reconstructed: {reconstructed}")
    print(f"   Echo status: {reconstructed.echo_activated}")

    # PART 9: Drift Simulation
    print_header("Temporal Drift: Evolution Through Time")

    print(f"\n{alexis.name}'s intent at t=0:")
    print(f"   [{alexis.intent.present:.2f}, "
          f"{alexis.intent.sequence:.2f}, {alexis.intent.future:.2f}]")

    # Simulate drift over time
    new_intent = [0.75, 0.65, 0.92]
    print(f"\nAfter experiencing the X-dimension (time), intent drifts to:")
    print(f"   {new_intent}")

    alexis.drift_state(new_intent)

    print(f"\nNew intent vector:")
    print(f"   [{alexis.intent.present:.2f}, "
          f"{alexis.intent.sequence:.2f}, {alexis.intent.future:.2f}]")

    # Check how kin relationships changed
    print("\nRecalculating kin after drift...")
    new_kin = alexis.sense_kin(candidates)
    print(f"Kin count: {len(kin)} → {len(new_kin)}")

    # PART 10: Summary
    print_header("Summary: The ART Friggitelli Philosophy")

    print("""
The EchoMage system implements core principles:

✅ "Strangers Who Know Each Other"
   - High similarity (knowing) but not identical (strangers)
   - Prevents stasis (too similar) and chaos (too different)
   - Generates productive creative friction

✅ Managing the Guest List
   - sense_kin() identifies optimal resonance
   - Excludes twins (stasis risk) and opposites (chaos risk)
   - Maintains network coherence

✅ The Continuous Party
   - ResonanceNetwork manages all entities
   - Echo pulses create network awareness
   - Drift tracking follows evolution through time

✅ LexOS Integration
   - Entities stored as quantum seeds
   - Manifestable in any format
   - Entanglement tracking for relationships

This is cultivation, not consumption.
This is the baker's art, not the blacksmith's grind.

🎉 The continuous party has started. Go cultivate!
""")

    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
