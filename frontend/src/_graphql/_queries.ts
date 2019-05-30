import gql from "graphql-tag";

export const ALL_MOVIES = gql`
  query allMovies {
    allMovies(first: 100) {
      edges {
        node {
          id
          name
          genres {
            id
            name
          }
        }
        cursor
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
`;
