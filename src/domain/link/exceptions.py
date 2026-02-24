class LinkNotFoundError(Exception):

    def __init__(self, link_id: int) -> None:
        super().__init__(self, f"Link id={link_id} not found")
        self.link_in = link_id