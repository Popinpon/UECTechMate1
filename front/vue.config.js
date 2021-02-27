module.exports = {
  assetsDir: 'static',
  devServer: {
    port: 8080,
    host: '127.0.0.1',
    proxy: {
      "/": {
        target: "http://localhost:5000",
      }
    }
  }
}
