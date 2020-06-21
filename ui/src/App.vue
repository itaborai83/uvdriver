<template>
	<div id="app">
		<sidebar/>
		<contents/>
	</div>
</template>

<script>
import SideBar from './components/SideBar.vue'
import Contents from './components/Contents.vue'

export default {
  name: 'App',
  components: {
	'sidebar'  : SideBar,
	'contents' : Contents
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
