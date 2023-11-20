const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  lintOnSave: false,
  transpileDependencies: true
})

module.exports = {
  devServer: {
    // disableHostCheck: true,
    proxy: {
      '/': {
        target: 'http://localhost:5000',
        ws: false,
        changOrigin: true,
        pathRewrite: {
          '^/': '/'
        }
      }
    }
  }
}
