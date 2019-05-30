<template>
  <v-container class="movie_list grid-list-xl">
    <v-layout wrap>
      <v-flex xs12>
        <v-card dark color="indigo lighten-2">
          <v-card-title primary-title>
            <h1 class="mr-4">Hot Tips</h1>
            <div>
              それぞれ設定してください。
            </div>
          </v-card-title>
        </v-card>
      </v-flex>

      <!-- <v-flex>
        <MovieList :movies="allMovies" @click-movie="openMovie" :loading="loading" />
      </v-flex> -->
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
// import MovieList from "@/components/MovieList.vue";
// import { Movie } from "@/types/models";
// import { ALL_MOVIES } from "@/graphql/queries";
// import {
//   allMovies_allMovies,
//   allMovies,
// } from '@/graphql/types/allMovies';

@Component({
  // components: {
  //   MovieList
  // },
  // apollo: {
  //   clientConfigs: {
  //     default: {
  //       httpEndpoint:
  //         "https://localhost:8000/dev/graphql",
  //       inMemoryCacheOptions: {
  //         freezeResults: false
  //       }
  //     }
  //   },
  //   allMovies: {
  //     query: ALL_MOVIES,
  //     update: (data) => {
  //       if (data.allMovies && data.allMovies.edges) {
  //         return data.allMovies.edges.map((edge: any) => edge.node);
  //       } else {
  //         return [];
  //       }
  //     }
  //   }
  // }
})
export default class Movies extends Vue {
  // allMovies!: Movie[];

  // mounted() {
  //   // ページ遷移時に内容を確実に更新
  //   this.$apollo.queries.allMovies.refetch();
  // }

  // get loading(): boolean {
  //   return this.$apollo.queries.allMovies.loading;
  // }

  // openMovie(movie: Movie) {
  //   this.$router.push({ name: "movie", params: { movieId: movie.id } });
  // }
}
</script>
