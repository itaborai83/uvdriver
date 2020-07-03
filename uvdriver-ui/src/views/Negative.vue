<template>
  <div class="container mt-3">
    <div class="row mb-3">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header"> <h2> Geração de Negativo </h2> </div>
          <div class="card-body">
            <div class="form-group">
              <div class="custom-file">
                <input type="file" class="custom-file-input" id="fileImage" v-on:change="validateFile($event)">
                <label class="custom-file-label" for="fileImage">Escolher Imagem</label>
              </div>
            <div class="text-center text-danger"> <strong> {{ lblErrorFile }} </strong> {{ fileImage }}</div>
              <input class="form-control mt-3" type="submit">
              <div class="text-center text-danger"> <strong> {{ lblErrorSubmit }} </strong> </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-sm-12"> 
        <div class="card-deck">
          <div class="card shadow-sm">
            <div class="card-header">
              <h5 class="card-title"> Ajustes de Tonalidade  </h5>
            </div>
            <div class="card-body">
              <div class="form-group">
                <label for="gammaSlider">Correção de Gamma - <strong>{{ gammaSlider }}</strong></label>
                <input type="range" class="form-control-range" id="gammaSlider" min="0.33" max="3.0" step="0.01" v-model="gammaSlider">
              </div>
              <div class="form-group">
                <label for="blackSlider">Remapemanto de Preto - <strong>{{ blackSlider }}</strong></label>
                <input type="range" class="form-control-range" id="blackSlider" min="0" max="255" v-model="blackSlider">
              </div>
             <div class="form-group">
                <label for="whiteSlider">Remapeamento de Branco - <strong> {{ whiteSlider }} </strong></label>
                <input type="range" class="form-control-range" id="whiteSlider" min="0" max="255" v-model="whiteSlider">
              </div>
              <div class="form-group">
                <input type="checkbox" class="form-control-input" id="chkEqualize" v-model="chkEqualize">
                <label for="chkEqualize">Aplicar Equalização de Histograma</label>
              </div>
            </div>
          </div>
        
        <div class="card shadow-sm">
          <div class="card-header">
            <h5 class="card-title"> Controle de Saída </h5>
          </div>
          <div class="card-body">
            <div class="form-group">
              <label>Tamanho Negativo</label>
              <div class="custom-control custom-radio custom-control-inline w-100">
                <select class="custom-select w-100" v-model="slctSize">
                  <option value="original">Original</option>
                  <option value="a3">A3</option>
                  <option value="a4">A4</option>
                  <option value="a5">A5</option>
                  <option value="a6">A6</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label for="borderSlider">Borda  - <strong>{{ borderSlider }}% </strong></label>
                <input type="range" class="form-control-range" id="borderSlider" min="0" max="50" v-model="borderSlider">
            </div>
          <div class="form-group">
            <label for="dpiSlider">DPI - <strong>{{ dpiSlider }}</strong></label>
            <input type="range" class="form-control-range" id="borderSlider" min="60" max="600" v-model="dpiSlider">
          </div>
        </div>
      </div>
     </div> 
   </div>
  </div>  
</div>
 
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Negative',
  data: function() {
    return {
      fileImage: "",
      lblErrorFile: "...",
      lblErrorSubmit: "...",
      gammaSlider: 1.0,
      blackSlider: 0,
      whiteSlider: 255,
      slctSize: "original",
      borderSlider: 5,
      dpiSlider: 300,
      chkEqualize: true
    }
  },
  components: {
  },
  methods: {
    validateFile: function($event) { 
      this.fileImage = $event.target.value;    
    }
  }
}
</script>
