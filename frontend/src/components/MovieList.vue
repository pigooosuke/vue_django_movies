<template>
  <v-data-table
    :headers="headers"
    :items="movies"
    :loading="loading"
    no-data-text="なし"
    class="elevation-1"
    hide-actions
    disable-initial-sort
  >
    <template v-slot:items="props">
      <tr span @click="clickMovie(props.item)">
        <td>{{ props.item.id }}</td>
        <td class="text-sm-left text-wrap">{{ props.item.name }}</td>
      </tr>
    </template>
  </v-data-table>
</template>

<script lang="ts">
import { Component, Prop, Emit, Vue } from "vue-property-decorator";
import { Movie } from "@/types/models";

@Component({})
export default class MovieList extends Vue {
  $refs!: {
    form: HTMLFormElement;
  };

  readonly headers = [
    { text: "ID", value: "id", width: "30" },
    { text: "名前", value: "name" }
  ];

  @Prop() movies!: Movie[];
  @Prop() loading!: boolean;

  @Emit()
  clickMovie(channel: Movie) {
    return channel;
  }
}
</script>

<style>
.text-wrap {
  word-break: break-all;
}
</style>
