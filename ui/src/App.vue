<template>
	<div id="app">
        <Header/>
		<NavBar v-bind:selected="selected" @sel-nav="handleNav"/>
		<Contents v-bind:selected="selected"/>
	</div>
</template>

<script>
import Header from './components/Header.vue'
import NavBar from './components/NavBar.vue'
import Contents from './components/Contents.vue'

export default {
  name: 'App',
  data: function(){
    return {
        selected: 'home'
    }
  },
  components: {
	Header,
    NavBar,
	Contents
  },
  methods: {
    handleNav: function(selectedItem) { this.selected = selectedItem; }
  }
}
</script>

<style>
#app {
  display: flex;
  align-items: stretch;
  flex-wrap: wrap;
  align-content: stretch;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
