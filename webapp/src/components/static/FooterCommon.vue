<template lang="">
    <footer class="footerConteinerTotal">
        <div class="footerConteinerDivs">        
            <div class="footerLinks"><a href="">Home</a></div>
            <div class="footerLinks"><a href="">About US</a></div>
            <div class="footerLinks"><a href="">Terms and Conditions</a></div>
        </div>
        <div class="footerCompanyInc">
            <p>© 2022 Company, Inc</p>
        </div>
    </footer>
</template>
<script>
export default {
    
}
</script>
<style>
    
.footerConteinerTotal {
    position: absolute;
    bottom: 0; 
    width: 100%;
    display: flex;
    flex-direction: column;
}

.footerConteinerDivs {
    background-color: white;
    display: flex;
    justify-content: center;
}

.footerLinks {
    background-color: white;
    display: flex;
    justify-content: center;
    width: 200px;
    padding: 20px;
}

.footerCompanyInc {
    background-color:white;
    display: flex;
    justify-content: center;
    padding: 20px;
}  
    
</style>