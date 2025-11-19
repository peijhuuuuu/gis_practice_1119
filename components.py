import solara
import ipyleaflet as leaflet
@solara.component
def IntroSection():
    polygon_layer = leaflet.GeoJSON(
        data=open("data/mata_an_river.geojson").read()
    )

    return StorySection(
        "馬太鞍溪流域介紹",
        "馬太鞍溪位於花蓮縣光復鄉，為中央山脈東側的一條重要河川...",
        layer=polygon_layer
    )
