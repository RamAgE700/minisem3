from django.db import models

# Model to store the PC specifications and game details
class GameOptimization(models.Model):
    # Basic information about the game and system
    game_title = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    ram = models.PositiveIntegerField()  # Amount of RAM in GB
    resolution = models.CharField(max_length=50)
    
    # The optimized settings from the API response
    optimized_settings = models.JSONField(null=True, blank=True)  # Store optimized settings as JSON

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game_title} ({self.cpu}, {self.gpu}, {self.ram}GB, {self.resolution})"
