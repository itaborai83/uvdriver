module.exports = {
    publicPath: process.env.NODE_ENV === "production" ? "/" : "/",
    outputDir: "dist",
    assetsDir: "",
    indexPath: "index.html",
    pages: {
        index: {
            entry: "src/pages/index/main.js",
            template: "public/index.html",
            filename: "index.html",
            title: "Home",
            chunks: [ "chunk-vendor", "chunk-common", "index" ]
        },
        negative: {
            entry: "src/pages/negative/main.js",
            template: "public/index.html",
            filename: "index.html",
            title: "Negativo",
            chunks: [ "chunk-vendor", "chunk-common", "index" ]
        }
    }
    /*
    devServer: {
        proxy: "http://locahost:4000"
    }
    */
}
