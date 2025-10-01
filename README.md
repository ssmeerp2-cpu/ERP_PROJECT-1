# ERP Project

This project is a Django-based ERP system designed to facilitate data entry and reporting for painter production. It includes a web interface for users to input data and an API for data management.

## Project Structure

```
erp_project
├── erp_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── erp_app
│   ├── __init__.py
│   ├── admin.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── filled_sheet.html
│   │   └── Reporting.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd erp_project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Update the `settings.py` file:
   - Add `erp_app` to the `INSTALLED_APPS` list.
   - Configure static and media files if necessary.

## Database Setup

1. Define the data models in `models.py`. For example:
   ```python
   from django.db import models

   class PainterEntry(models.Model):
       painter_name = models.CharField(max_length=100)
       date = models.DateField()
       part_no = models.CharField(max_length=100)
       grn_no = models.CharField(max_length=100)
       # Add other fields as necessary
   ```

2. Create serializers in `serializers.py`:
   ```python
   from rest_framework import serializers
   from .models import PainterEntry

   class PainterEntrySerializer(serializers.ModelSerializer):
       class Meta:
           model = PainterEntry
           fields = '__all__'
   ```

3. Create API views in `views.py`:
   ```python
   from rest_framework import viewsets
   from .models import PainterEntry
   from .serializers import PainterEntrySerializer

   class PainterEntryViewSet(viewsets.ModelViewSet):
       queryset = PainterEntry.objects.all()
       serializer_class = PainterEntrySerializer
   ```

4. Update `urls.py` to include API routes:
   ```python
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .api.views import PainterEntryViewSet

   router = DefaultRouter()
   router.register(r'entries', PainterEntryViewSet)

   urlpatterns = [
       path('api/', include(router.urls)),
       # Add other URL patterns
   ]
   ```

## Running the Application

1. Run migrations to create the database tables:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Start the Django development server:
   ```
   python manage.py runserver
   ```

3. Use Ngrok to expose your local server to the internet:
   ```
   ngrok http 8000
   ```

4. Share the provided Ngrok URL for external access.

## Testing

- Test the API endpoints and the HTML form to ensure data is being saved and retrieved correctly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.