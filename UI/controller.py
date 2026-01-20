import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare i dropdown """
        # TODO
        years = self._model.get_years()
        for year in years :
            self._view.dd_year.options.append (ft.dropdown.Option (year))

        shapes = self._model.get_shapes()

        for shape in shapes :
            if shape is not None :
                self._view.dd_shape.options.append (ft.dropdown.Option (shape))
        self._view.page.update ()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        # TODO
        self._view.lista_visualizzazione_1.clean ()
        self._model._G.clear ()

        self._model.build_graph()
        nodes = self._model._nodes
        edges = self._model._edges

        year = self._view.dd_year.value
        shape = self._view.dd_shape.value

        map_weight = self._model.get_weights (year, shape)

        self._view.lista_visualizzazione_1.controls.append (
            ft.Text (f"Il numero di nodi presenti nel grafo è {self._model._G.number_of_nodes()}"))
        self._view.lista_visualizzazione_1.controls.append(
            ft.Text(f"Il numero di archi presenti nel grafo è {len(edges)}."))

        for edge in edges :
            self._view.lista_visualizzazione_1.controls.append (
                ft.Text (f"Nodo: {edge [0]}, somma pesi su archi = {map_weight [edge]}"))
        self._view.page.update ()



    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
