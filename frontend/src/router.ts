import Vue from "vue";
import Router from "vue-router";
import MovieListPage from "./views/MovieListPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      redirect: { name: "movies" }
    },
    {
      path: "/movies",
      name: "movies",
      component: MovieListPage
    }
  ]
});
