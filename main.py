import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE, WINDOW_TITLE, COLOR_BACKGROUND
from animations import FloatingHeart
from renderer import draw_3d_text

def main() -> None:
    """Main execution loop for the Ali Birthday Celebration display."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    
    heartfelt_wish = """ALI BAHI APKO APKI SALGIRAH MUBARAK HO BUT AGAR AP MUJ PY YAQEEN KARKY MUJY APNI FB KI ID LOGIN DETY TO MA PICS LA KY AUR ACHI WEBSITE BANATA KAHIR CHORO ALLAH APKO KAMAYAB کARY AGA KI MANZIALAIN ASAN کRY OR HAMARAI DOSTI KAIM کRY BAKI LOVE YOU HOGYA <3"""
    
    clock = pygame.time.Clock()

    # Initialize heart particles
    hearts = [FloatingHeart() for _ in range(30)]

    running = True
    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update State
        for heart in hearts:
            heart.update()

        # 3. Rendering
        screen.fill(COLOR_BACKGROUND)

        # Draw hearts behind text
        for heart in hearts:
            screen.blit(heart.surface, (heart.x, heart.y))

        # Draw main 3D text
        draw_3d_text(screen)
        
        # Render the heartfelt wish message underneath "Ali"
        # Adjusted to move lower and include a bounding box
        font = pygame.font.SysFont("Arial", 22)
        words = heartfelt_wish.split(' ')
        lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if font.size(' '.join(current_line))[0] > SCREEN_WIDTH - 150:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        line_height = 30
        total_text_height = len(lines) * line_height
        
        # Box dimensions and position
        box_width = SCREEN_WIDTH - 100
        box_height = total_text_height + 40
        box_x = (SCREEN_WIDTH - box_width) // 2
        box_y = (SCREEN_HEIGHT // 2) + 100  # Pushed further down
        
        # Draw the distinct rectangular box
        pygame.draw.rect(screen, (0, 0, 0, 150), (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height), 2)

        # Render lines inside the box
        text_y_offset = box_y + 20
        for line in lines:
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, text_y_offset))
            screen.blit(text_surface, text_rect)
            text_y_offset += line_height

        pygame.display.flip()
        clock.tick(FRAME_RATE)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()