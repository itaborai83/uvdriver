<template>
	<div id="app">
       Hello World 
	</div>
</template>

<script>

export default {
  name: 'App',
  data: function(){
    return {
    }
  },
  components: {
  },
  methods: {
    handleNav: function(selectedItem) { this.selected = selectedItem; }
  }
}
</script>

<style scoped>
#app {
 font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
