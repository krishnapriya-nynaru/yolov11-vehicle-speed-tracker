import supervision as sv
from utils.constants import POLYGON

def create_zone():
    return sv.PolygonZone(POLYGON, (sv.Position.TOP_CENTER, sv.Position.BOTTOM_CENTER))
