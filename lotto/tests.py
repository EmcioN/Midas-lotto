from django.test import TestCase
from django.urls import reverse
from lotto.models import MonthlySummary, Draw


class LottoPageTests(TestCase):
    def setUp(self):
        self.month = MonthlySummary.objects.create(
            month=4, year=2026, total_winnings=100, subscription_price=20
        )
        self.draw = Draw.objects.create(
            monthly_summary=self.month,
            title="April Draw 1",
            draw_date="2026-04-03",
            draw_number=1,
            winnings_amount=25,
            is_current=True,
        )

    def test_draw_list_page_loads(self):
        response = self.client.get(reverse("draw_list"))
        self.assertEqual(response.status_code, 200)

    def test_draw_detail_page_loads(self):
        response = self.client.get(reverse("draw_detail", args=[self.draw.id]))
        self.assertEqual(response.status_code, 200)
