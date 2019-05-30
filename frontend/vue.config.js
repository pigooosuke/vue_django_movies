//
// vue.confg.js
//

module.exports = {
  devServer: {
    proxy: {
      "^/(login|logout|social|graphql|admin|static/admin)": {
        target: "http://localhost:8000",
        changeOrigin: true
      }
    }
  },
  configureWebpack: {
    devtool: "source-map"
  },

  outputDir: "dist/",
  assetsDir: "static/",
  indexPath: "index.html"
};
