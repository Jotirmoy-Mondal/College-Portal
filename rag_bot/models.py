from django.db import models

class CollegeDocument(models.Model):
     #this create a new db table with the class name
    # The name of the file (e.g., "Computer Science Syllabus")
    title = models.CharField(max_length=255)
    
    # Metadata for Slot Filling (e.g., "Computer Science", "4th")
    department = models.CharField(max_length=100, blank=True)
    semester = models.CharField(max_length=50, blank=True)
    
    # The actual PDF file itself
    pdf_file = models.FileField(upload_to='documents/')
    
    # A timestamp of when you uploaded it
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # This makes the document look nice in the admin dashboard
    def __str__(self):
        return self.title