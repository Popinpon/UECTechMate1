// プラグイン
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");

module.exports = {
  mode: 'development',
  entry: './src/main.ts',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '../dist/static')
  },
  module:{
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: "ts-loader",
        exclude: "/node_modules/",
        options: {
          appendTsSuffixTo: [/\.vue$/]
        }
      },
      {
        test: /\.vue$/,
        loader: "vue-loader"
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader, { loader: "css-loader", options: { importLoaders: 1 } } ,{ loader: "postcss-loader" }
        ]
      },
      {
        test: /\.(jpg|png|gif)$/,
        use: [
            {
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]',
                    outputPath : 'img/',
                    esModule: false,
                    publicPath : function(path){
                        return '../' + path;
                    }
                  }
            }
        ]
      },
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new MiniCssExtractPlugin(),
  ],
  // ts 用だけど、とりあえず保留
  resolve: {
    alias: {
      vue$: "vue/dist/vue.esm.js"
    },
    extensions: [".ts", ".tsx", ".vue", ".js", ".jsx", ".json"],
  },
  // optimization: {
  //   minimizer: [new OptimizeCSSAssetsPlugin({})],
  // },
  devServer: {
    // サーバーの起点ディレクトリ
    // contentBase: "dist",
    // バンドルされるファイルの監視 // パスがサーバー起点と異なる場合に設定
    publicPath: '/dist',
    //コンテンツの変更監視をする
    watchContentBase: true,
    // 実行時(サーバー起動時)ブラウザ自動起動
    open: true,
    // 自動で指定したページを開く
    openPage: "index.html",
    //　同一network内からのアクセス可能に
    host: "0.0.0.0"
  }
};