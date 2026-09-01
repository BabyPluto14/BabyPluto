const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://'+path.resolve(__dirname,'study_guide_unit4.html'), {waitUntil:'networkidle'});
  await pg.pdf({ path: path.resolve(__dirname,'Microeconomics_Unit4_Study_Guide.pdf'),
    printBackground:true, preferCSSPageSize:true, margin:{top:'0',bottom:'0',left:'0',right:'0'} });
  await b.close(); console.log('PDF generated.');
})();
