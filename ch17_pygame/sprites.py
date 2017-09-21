gravity = 0.01


class QueenSprite:

    def __init__(self, img, target_position):
        """
        Create and initialize a queen for this
        target on the board.
        """
        self.image = img
        self.target_position = target_position
        (x, y) = target_position
        self.posn = (x, 0)  # Start ball at top of its column
        self.y_velocity = 0  # with zero initial velocity

    def update(self):
        self.y_velocity += gravity  # Gravity changes velocity
        (x, y) = self.posn
        new_y_posn = y + self.y_velocity  # Velocity move the ball
        (target_x, target_y) = self.target_position  # Unpack the position
        distance_to_go = target_y - new_y_posn  # How far to our floor?

        if distance_to_go < 0:  # Are we under the floor?
            self.y_velocity = -0.65 * self.y_velocity  # Bounce
            new_y_posn = target_y + distance_to_go  # Move back above floor

        self.posn = (x, new_y_posn)  # Set our new position

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt. """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.8  # Kick it up in air


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count + 1) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0, 50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt. """
        (my_x, my_y) = self.posn
        my_width = 50
        my_height = self.image.get_height()
        (x, y) = pt
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)


class Cards:

    def __init__(self, img, curr_x, curr_y):
        self.image = img
        self.curr_patch_num_x = curr_x
        self.curr_patch_num_y = curr_y

    def draw(self, target_surface, position, width, height):
        patch_rect = (self.curr_patch_num_x * width,
                      self.curr_patch_num_y * height,
                      width, height)
        target_surface.blit(self.image, position, patch_rect)

    def contains_point(self, pt, position, my_width, my_height):
        """ Return True if my sprite rectangle contains point pt. """
        (my_x, my_y) = position
        (x, y) = pt
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)
