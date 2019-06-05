<template>
  <v-container class="movie_list grid-list-xl" fluid>
    <v-layout wrap>
      <v-flex>
        <MovieList
          :movies="allMovies"
          @click-movie="openMovie"
          :loading="loading"
        />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import MovieList from "@/components/MovieList.vue";
import { Movie } from "@/types/models";
import { ALL_MOVIES } from "@/graphql/queries";
import { allMovies_allMovies, allMovies } from "@/graphql/types/allMovies";

@Component({
  components: {
    MovieList
  },
  apollo: {
    allMovies: {
      query: ALL_MOVIES,
      update: (data: allMovies) => {
        if (data.allMovies && data.allMovies.edges) {
          return data.allMovies.edges.map((edge: any) => edge.node);
        } else {
          return [];
        }
      }
    }
  }
})
export default class Movies extends Vue {
  allMovies!: Movie[];
  mounted() {
    this.$apollo.queries.allMovies.refetch();
  }
  get loading(): boolean {
    return this.$apollo.queries.allMovies.loading;
  }
  openMovie(movie: Movie) {
    this.$router.push({ name: "movie", params: { movieId: movie.id } });
  }
}
</script>
