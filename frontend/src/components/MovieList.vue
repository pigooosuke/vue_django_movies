<template>
  <v-layout wrap justify-space-around>
    <v-flex v-for="movie in movies" :key="movie.id">
      <v-card color="gray" dark width="220px">
        <v-card-text>{{ movie.name }}</v-card-text>
        <v-responsive height="220px"></v-responsive>
        <v-card-actions>
          <div id="chip-usage-example" class="text-xs-center">
            <v-chip v-for="genre in movie.genres" :key="genre.id">
              {{ genre.name }}
            </v-chip>
          </div>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import { Movie } from "@/types/models";

@Component({})
export default class MovieList extends Vue {
  $refs!: {
    form: HTMLFormElement;
  };

  @Prop() movies!: Movie[];
  @Prop() loading!: boolean;

  @Emit()
  clickMovie(movie: Movie) {
    return movie;
  }
}
</script>

<style>
.text-wrap {
  word-break: break-all;
}
</style>
