import random
import pygame
from math import sin, pi
from typing import List, Dict
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, HEART_COUNT,
    HEART_SIZE_MIN, HEART_SIZE_MAX,
    HEART_SPEED_Y_MIN, HEART_SPEED_Y_MAX,
    HEART_SPEED_X_MAX, COLOR_HEART,
    HEART_ALPHA_MIN, HEART_ALPHA_MAX
)

class FloatingHeart:
    """Represents a single heart particle with smooth floating animation."""

    def __init__(self) -> None:
        self.size = random.randint(HEART_SIZE_MIN, HEART_SIZE_MAX)
        self.x = random.uniform(0, SCREEN_WIDTH)
        # Start slightly below the screen
        self.y = random.uniform(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.speed_y = random.uniform(HEART_SPEED_Y_MIN, HEART_SPEED_Y_MAX)
        # Horizontal movement properties
        self.drift_speed = random.uniform(0.5, HEART_SPEED_X_MAX)
        self.drift_phase = random.uniform(0, 2 * pi)
        # Opacity variation
        self.alpha = random.randint(HEART_ALPHA_MIN, HEART_ALPHA_MAX)
        self.surface = self._create_heart_surface()

    def _create_heart_surface(self) -> pygame.Surface:
        """Draws the fixed heart graphic onto a transparent surface."""
        # A simple heart using two circles and a triangle, or standard primitives
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        # Base color with randomized alpha
        color = (*COLOR_HEART, self.alpha)
        
        # Center points for geometric drawing
        cx = self.size // 2
        cy = float(self.size) * 0.4
        r = float(self.size) // 3.5

        # Draw left and right curves of the heart
        pygame.draw.circle(surf, color, (int(cx - r), int(cy)), int(r))
        pygame.draw.circle(surf, color, (int(cx + r), int(cy)), int(r))
        
        # Draw bottom point (triangle approximation)
        points = [
            (float(cx - 2.0 * r), cy),
            (float(cx + 2.0 * r), cy),
            (float(cx), float(self.size) * 0.95)
        ]
        pygame.draw.polygon(surf, color, points)
        
        return surf

    def update(self) -> None:
        """Updates the position and oscillation of the heart."""
        # Move up
        self.y -= self.speed_y
        
        # Horizontal oscillation (creates floaty/drunken effect)
        self.drift_phase += 0.02
        dx = sin(self.drift_phase) * self.drift_speed
        self.x += dx

        # Reset if it goes off top
        if self.y < -self.size:
            self.y = SCREEN_HEIGHT + random.uniform(10, 50)
            self.x = random.uniform(0, SCREEN_WIDTH)

class AnimationManager:
    """Manages a collection of FloatingHeart animations."""

    def __init__(self) -> None:
        self.hearts: List[FloatingHeart] = [FloatingHeart() for _ in range(HEART_COUNT)]

    def update_hearts(self) -> None:
        """Updates physics and state for all hearts."""
        for heart in self.hearts:
            heart.update()

    def get_drawn_surfaces() -> List[Dict[str, object]]:
        """Returns ready-to-draw pre-rendered surfaces and positions."""
        # Returns List containing {'surf': Surface, 'rect': (x,y)}
        results = []
        for heart in self.hearts:
            results.append({
                'surf': heart.surface,
                'pos': (int(heart.x), int(heart.y))
            })
        return results

# Initialize internal state
_manager = AnimationManager()

def update_animations() -> None:
    """Updates global animation state."""
    _manager.update_hearts()

def get_heart_surfaces() -> List[Dict[str, object]]:
    """Returns list of heart surfaces and their positions for rendering."""
    return _manager.get_drawn_surfaces()