from django.test import TestCase
from erp_app.models import PainterEntry

class PainterEntryModelTest(TestCase):

    def setUp(self):
        PainterEntry.objects.create(
            painter_name="John Doe",
            date="2023-10-01",
            part_no="Part123",
            grn_no="GRN456"
        )

    def test_painter_entry_creation(self):
        entry = PainterEntry.objects.get(part_no="Part123")
        self.assertEqual(entry.painter_name, "John Doe")
        self.assertEqual(entry.date, "2023-10-01")
        self.assertEqual(entry.part_no, "Part123")
        self.assertEqual(entry.grn_no, "GRN456")

class PainterEntryAPITest(TestCase):

    def setUp(self):
        self.entry = PainterEntry.objects.create(
            painter_name="Jane Smith",
            date="2023-10-02",
            part_no="Part789",
            grn_no="GRN012"
        )

    def test_api_get_entries(self):
        response = self.client.get('/api/entries/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Smith")

    def test_api_create_entry(self):
        response = self.client.post('/api/entries/', {
            'painter_name': 'Alice Johnson',
            'date': '2023-10-03',
            'part_no': 'Part456',
            'grn_no': 'GRN789'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PainterEntry.objects.count(), 2)
        self.assertEqual(PainterEntry.objects.get(part_no='Part456').painter_name, 'Alice Johnson')