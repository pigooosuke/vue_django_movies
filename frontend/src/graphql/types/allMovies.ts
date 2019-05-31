/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: allMovies
// ====================================================

export interface allMovies_allMovies_edges_node_genres {
  /**
   * The ID of the object.
   */
  id: string;
  name: string;
}

export interface allMovies_allMovies_edges_node {
  /**
   * The ID of the object.
   */
  id: string;
  name: string;
  genres: allMovies_allMovies_edges_node_genres[];
}

export interface allMovies_allMovies_edges {
  /**
   * The item at the end of the edge
   */
  node: allMovies_allMovies_edges_node | null;
  /**
   * A cursor for use in pagination
   */
  cursor: string;
}

export interface allMovies_allMovies_pageInfo {
  /**
   * When paginating forwards, the cursor to continue.
   */
  endCursor: string | null;
  /**
   * When paginating forwards, are there more items?
   */
  hasNextPage: boolean;
}

export interface allMovies_allMovies {
  edges: (allMovies_allMovies_edges | null)[];
  pageInfo: allMovies_allMovies_pageInfo;
}

export interface allMovies {
  allMovies: allMovies_allMovies | null;
}
