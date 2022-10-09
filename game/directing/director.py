from os import remove
from game.shared.point import Point
from game.shared.color import Color
from game.casting.artifact import Artifact
from game.casting.cast import Cast
import random
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._falling_artifacts(cast)
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)
        X = robot.get_position().get_x()
        Y = robot.get_position().get_y()
        if robot.get_position().get_y() < 450:
            robot.set_position(Point(robot.get_position().get_x(),559))
        if robot.get_position().get_y() > 560:
            robot.set_position(Point(robot.get_position().get_x(),451))
        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            pos_x = robot.get_position().get_x()
            pos_y = robot.get_position().get_y()
            art_y = artifact.get_position().get_y()
            art_x = artifact.get_position().get_x()
            hit_x = pos_x - art_x
            hit_y = pos_y - art_y
            if (-10 < hit_x < 10) and (-10 < hit_y < 10):
                if artifact.get_text() == "o":
                    self._score += -1
                if artifact.get_text() == "*":
                    self._score += 1
                cast.remove_actor("artifacts", artifact)
        banner.set_text(f"Score: {self._score}")    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
    
    def _falling_artifacts(self, cast):
        """Makes the artifacts fall.
        
        Args:
            cast (Cast): The cast of actors.
        """
        artifacts = cast.get_actors("artifacts")
        for artifact in artifacts:
            artifact.set_position(artifact.get_position().add(Point(0,1)))
            if artifact.get_position().get_y() == 600:
                cast.remove_actor("artifacts", artifact)
        if len(artifacts) < 50:
            for i in range(1):
                COLS = 60
                ROWS = 40
                CELL_SIZE = 15
                FONT_SIZE = 15
                rock_gem = ["o","*"]
                text = rock_gem[random.randint(0,1)]

                x = random.randint(1, COLS - 1)
                y = (random.randint(0, 5))
                position = Point(x, y)
                position = position.scale(CELL_SIZE)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)

                artifact = Artifact()
                artifact.set_text(text)
                artifact.set_font_size(FONT_SIZE)
                artifact.set_color(color)
                artifact.set_position(position)
                #artifact.set_message(message)
                cast.add_actor("artifacts", artifact)