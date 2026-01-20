from curses.ascii import islower

import networkx as nx
from database.dao import DAO

class Model:
    def __init__ (self) :
        self._G = nx.Graph ()

        self._states_map = {}
        self.get_states ()

        self._nodes = self.get_states()
        self._edges = []
        for edge in self.get_edges() :
            self._edges.append (edge)

        self._map_edge_weight = {}

    @staticmethod
    def get_years () :
        results = []
        for year in DAO.load_years() :
            if year not in results :
                if int (year) >= 1910 and int (year) <= 2014 :
                    results.append (year)
        return results

    @staticmethod
    def get_shapes () :
        results = []
        sightings = DAO.load_sightings ()
        for sighting in sightings :
            if sighting.shape not in results :
                results.append (sighting.shape)
        return results

    def get_states (self) :
        results = []
        for state in DAO.load_states () :
            results.append (state)
            if state.neighbors is not None :
                self._states_map [state.id] = state.neighbors.split (" ")

        return results

    def get_edges (self) :
        results = []
        existing_edges = set(self._edges)
        for node_id, neighbors in self._states_map.items():
            for neighbor in neighbors:
                if (node_id, neighbor) not in existing_edges and (neighbor, node_id) not in existing_edges:
                    results.append((node_id, neighbor))
                    existing_edges.add((node_id, neighbor))
        return results

    def build_graph (self) :
        self._G.add_nodes_from(self._nodes)

    def get_weights (self, year, shape) :
        sightings = DAO.load_sightings ()

        for edge in self._edges :
            weight = 0
            for s in sightings :
                if s.state == edge[0].lower() or s.state == edge[1].lower() :
                    if s.shape == shape and int (s.s_datetime.year) == int (year) :
                        weight += 1

            self._map_edge_weight [edge] = weight

        return self._map_edge_weight
