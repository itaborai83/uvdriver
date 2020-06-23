<template>
	<div id="app">
		<sidebar v-bind:selected="selected" @sel-nav="handleNav"/>
		<contents v-bind:selected="selected"/>
	</div>
</template>

<script>
import SideBar from './components/SideBar.vue'
import Contents from './components/Contents.vue'

export default {
  name: 'App',
  data: function(){
    return {
        selected: 'home'
    }
  },
  components: {
	sidebar  : SideBar,
	contents : Contents
  },
  methods: {
    handleNav: function(selectedItem) { this.selected = selectedItem; }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
