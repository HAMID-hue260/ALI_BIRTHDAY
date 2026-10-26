import pygame
from typing import List, Dict
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TITLE_FONT,
    TEXT_CONTENT,
    COLOR_TEXT_MAIN,
    COLOR_TEXT_SHADOW,
    TEXT_DEPTH_OFFSET,
    COLOR_HEART
)

def draw_3d_text(surface: pygame.Surface) -> None:
    """
    Renders the main text with a 3D effect by layering shadows.

    Args:
        surface: The Pygame surface to draw onto.
    """
    text_surface_main = TITLE_FONT.render(TEXT_CONTENT, True, COLOR_TEXT_MAIN)
    text_surface_shadow = TITLE_FONT.render(TEXT_CONTENT, True, COLOR_TEXT_SHADOW)

    text_rect = text_surface_main.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Draw shadow layers for depth
    for i in range(1, TEXT_DEPTH_OFFSET + 1):
        shadow_rect = text_rect.copy()
        shadow_rect.x += i
        shadow_rect.y += i
        surface.blit(text_surface_shadow, shadow_rect)

    # Draw main text over shadows
    surface.blit(text_surface_main, text_rect)

def draw_heart(surface: pygame.Surface, x: float, y: float, size: int, alpha: int) -> None:
    """
    Draws a filled heart shape with specific size and alpha transparency.

    Args:
        surface: The Pygame surface to draw onto.
        x: Horizontal center position.
        y: Vertical center position.
        size: Width/height parameter for the heart.
        alpha: Transparency level (0-255).
    """
    heart_surf = pygame.Surface((size, size), pygame.SRCALPHA)
    
    # Simple heart shape constructed from two circles and a rotated square
    # Adjust coordinates relative to heart_surf center
    circle_center_dist = size // 4
    circle_radius = size // 4 + 1
    
    pygame.draw.circle(heart_surf, (*COLOR_HEART, alpha), (size // 4, size // 4 + circle_center_dist), circle_radius)
    pygame.draw.circle(heart_surf, (*COLOR_HEART, alpha), (size - size // 4, size // 4 + circle_center_dist), circle_radius)
    
    # Points for bottom triangle part
    points = [
        (size // 16, size // 2), 
        (size // 2, size - size // 16), 
        (size - size // 16, size // 2)
    ]
    pygame.draw.polygon(heart_surf, (*COLOR_HEART, alpha), points)

    # Draw centered
    rect = heart_surf.get_rect(center=(int(x), int(y)))
    surface.blit(heart_surf, rect)

def render_frame(surface: pygame.Surface, hearts: List[Dict[str, float]]) -> None:
    """
    Clears screen, renders textured background, 3D text, and all hearts.

    Args:
        surface: The Pygame screen surface.
        hearts: List of heart particle dictionaries containing state.
    """
    # Clear screen with background color in config is handled in main loop
    # or can re-fill here if screen is passed fresh each frame.
    
    # Render 3D text in center
    draw_3d_text(surface)

    # Render each heart
    for heart in hearts:
        draw_heart(
            surface,
            heart['x'],
            heart['y'],
            int(heart['size']),
            int(heart['alpha'])
        )