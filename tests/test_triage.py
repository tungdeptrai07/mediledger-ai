import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))
from triage_engine import run_ai_triage


class MediLedgerTriageTests(unittest.TestCase):
    def test_critical_cardiac_triage(self) -> None:
        res = run_ai_triage("did:med:test-1", ["chest_pain", "high_fever"], heart_rate_bpm=125, spo2_pct=91, temp_celsius=39.4)
        self.assertEqual(res["urgency_tier"], "CRITICAL_IMMEDIATE")
        self.assertGreaterEqual(res["risk_score"], 60)
        self.assertTrue(res["onchain_attestation_hash"].startswith("0x"))

    def test_routine_outpatient_triage(self) -> None:
        res = run_ai_triage("did:med:test-2", ["headache"], heart_rate_bpm=72, spo2_pct=99, temp_celsius=36.8)
        self.assertEqual(res["urgency_tier"], "ROUTINE_OUTPATIENT")
        self.assertEqual(res["recommended_department"], "General Practice")


if __name__ == "__main__":
    unittest.main()
