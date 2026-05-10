class Resultado:

    def __init__(self, season, round, race_name, driver_name, constructor, position):
        self.season = season
        self.round = round
        self.race_name = race_name
        self.driver_name = driver_name
        self.constructor = constructor
        self.position = position

    def __repr__(self):
        """Formal representation of result"""
        return (
            f"Resultado("
            f"season={self.season!r}, "
            f"round={self.round!r}, "
            f"race_name={self.race_name!r}"
            f"driver_name={self.driver_name!r}, "
            f"constructor={self.constructor!r}, "
            f"position={self.position!r}, "
            f")"
        )

    def __str__(self):
        """Return a readable representation of the result"""
        return (
            f"Temporada: {self.season} | Ronda: {self.round}\n"
            f"Carrera: {self.race_name} | Piloto: {self.driver_name}\n"
            f"Escuderia: {self.constructor} | Posicion: {self.position}\n"
        )