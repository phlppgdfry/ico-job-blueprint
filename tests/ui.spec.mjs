import {test,expect} from '@playwright/test';
test('Overview, search and all nine modules render; chapter progress persists',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('./');await expect(page).toHaveTitle(/ICO Job Blueprint/);await expect(page.getByRole('heading',{level:1})).toHaveText('IT Development Officer');
 for(const [name,title] of [['Technische kennis','Technische kennis'],['SOPs & incidenten','SOPs & incidenten'],['Scenario’s','Interactieve scenario’s'],['Interview','Interview simulator'],['Skills & bewijs','Skills & bewijs'],['Portfolio','Portfolio projecten'],['Leerroadmap','Leerroadmap'],['Carrière','Carrière']]){await page.getByRole('navigation').getByRole('button',{name,exact:true}).click();await expect(page.getByRole('heading',{level:1})).toHaveText(title);}
 await page.getByRole('searchbox').fill('reconciliatie');await expect(page.getByRole('heading',{level:1})).toHaveText('Zoekresultaten');await expect(page.locator('.search-results button')).not.toHaveCount(0);
 await page.locator('.search-results button').filter({hasText:'06 ·'}).first().click();await expect(page).toHaveURL(/chapter\/6\/\d+/);await expect(page.getByRole('heading',{level:1})).toHaveText('Technologiehandboek');
 await page.getByRole('checkbox',{name:'Bestudeerd'}).check();await page.reload();await expect(page.getByRole('checkbox',{name:'Bestudeerd'})).toBeChecked();
 await page.getByRole('button',{name:'Alles inklappen'}).click();await expect(page.locator('article details[open]')).toHaveCount(1);await page.getByRole('button',{name:'Alles uitklappen'}).click();
 await page.getByRole('navigation').getByRole('button',{name:'Overzicht',exact:true}).click();await expect(page.locator('.preparation h2')).toContainText('3%');
 await page.getByRole('searchbox').fill('zzzxxyy');await expect(page.locator('.empty')).toContainText('Geen resultaten');
 expect(errors).toEqual([]);
});
test('Checklists and notes persist through re-render and reload',async({page})=>{
 await page.goto('./#/chapter/11');await expect(page.getByRole('heading',{level:1})).toContainText('Incident, problem');
 const checks=page.getByRole('checkbox',{name:'Checklistpunt',exact:true});await expect(checks).toHaveCount(30);await checks.first().check();await expect(checks.first()).toBeChecked();
 await page.getByLabel('Mijn notities en open vragen').fill('Mijn eerste changevraag');await page.reload();await expect(checks.first()).toBeChecked();await expect(page.getByLabel('Mijn notities en open vragen')).toHaveValue('Mijn eerste changevraag');
});
test('Scenario and interview exercises store answers and rubric; timer and filtering work',async({page})=>{
 await page.goto('./#/scenarios');await expect(page.locator('.exercise-list>button')).toHaveCount(25);await page.getByLabel('Filter').selectOption('Specialistisch');await expect(page.locator('.exercise-list>button')).toHaveCount(3);
 await page.locator('.exercise-list>button').first().click();await page.getByLabel('Mijn antwoord').fill('Ik bepaal impact, snapshot en unieke sleutels vóór go-live.');await page.getByRole('button',{name:'Start timer'}).click();await expect(page.locator('.timer strong')).not.toHaveText('00:00',{timeout:5000});await page.getByRole('button',{name:'Pauze',exact:true}).click();
 await page.getByRole('button',{name:'Bekijk rubric & modelantwoord'}).click();await page.locator('.rubric input').first().check();await expect(page.locator('.feedback')).toContainText('1 / 4');await page.reload();await expect(page.getByLabel('Mijn antwoord')).toContainText('snapshot');await page.getByRole('button',{name:'Bekijk rubric & modelantwoord'}).click();await expect(page.locator('.rubric input').first()).toBeChecked();
 await page.goto('./#/interview');await expect(page.locator('.exercise-list>button')).toHaveCount(56);await page.getByLabel('Filter').selectOption('Techniek');await expect(page.locator('.exercise-list>button')).toHaveCount(7);await page.locator('.exercise-list>button').first().click();await page.getByLabel('Mijn antwoord').fill('Ik onderscheid bevestigde componenten van topologie.');await page.getByRole('button',{name:'Bekijk rubric & modelantwoord'}).click();await expect(page.locator('.feedback')).toContainText('Wat wil de interviewer weten?');await page.reload();await expect(page.getByLabel('Mijn antwoord')).toContainText('topologie');
});
test('Skills, requirement evidence, roadmap, export/import and theme persist',async({page})=>{
 await page.goto('./#/skills');await page.getByLabel('Mijn niveau SQL / relationele data').selectOption('Met hulp uitvoeren');await page.getByLabel('Bewijs SQL / relationele data').fill('Lab met 20 voertuigen, query-tests en README.');await page.locator('.requirements-tracker details').first().locator('summary').click();await page.getByLabel('Bewijs R01').fill('Praktische context te bespreken');await page.reload();await expect(page.getByLabel('Mijn niveau SQL / relationele data')).toHaveValue('Met hulp uitvoeren');
 await page.goto('./#/roadmap');await page.getByRole('checkbox',{name:'Dag 1 afgerond',exact:true}).check();await page.reload();await expect(page.getByRole('checkbox',{name:'Dag 1 afgerond',exact:true})).toBeChecked();
 await page.getByRole('button',{name:'Dark mode inschakelen'}).click();await page.reload();await expect(page.locator('html')).toHaveAttribute('data-theme','dark');
 const waiting=page.waitForEvent('download');await page.getByRole('button',{name:'Exporteer voortgang'}).click();const downloaded=await waiting;const path=await downloaded.path();expect(downloaded.suggestedFilename()).toBe('ico-role-os-voortgang.json');
 await page.locator('input[type=file]').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer:Buffer.from('{"schema":2}')});await expect(page.getByRole('status')).toContainText('Import niet uitgevoerd');
 await page.locator('input[type=file]').setInputFiles(path);await expect(page.getByRole('status')).toContainText('Voortgang geïmporteerd');
});
test('Every chapter and source dossier render with real content',async({page})=>{
 for(let i=1;i<=30;i++){await page.goto(`./#/chapter/${i}`);await expect(page.getByRole('heading',{level:1})).not.toBeEmpty();await expect(page.locator('.prose').first()).toContainText(/vacature|functie|context|profiel|Compacte|Waarschijnlijk/i);}
 await page.goto('./#/sources');await expect(page.getByRole('heading',{level:1})).toHaveText('Bronnen & betrouwbaarheid');await expect(page.getByRole('link',{name:'Vacature IT Development Officer'})).toHaveAttribute('href','https://www.icoterminals.com/nl/jobs/it-development-officer');
});
test('Mobile drawer, dark/light, content widths and practice work at 390px',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto('./');await expect(page.getByRole('heading',{level:1})).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
 await page.getByRole('button',{name:'Menu openen'}).click();await expect(page.locator('.sidebar')).toHaveClass(/is-open/);await page.keyboard.press('Escape');await expect(page.locator('.sidebar')).not.toHaveClass(/is-open/);
 await page.getByRole('button',{name:'Menu openen'}).click();await page.getByRole('navigation').getByRole('button',{name:'Scenario’s',exact:true}).click();await expect(page.getByRole('heading',{level:1})).toHaveText('Interactieve scenario’s');await expect(page.locator('.sidebar')).not.toHaveClass(/is-open/);await page.locator('.exercise-list>button').first().click();await page.getByLabel('Mijn antwoord').fill('Mobiele aanpak');await page.getByRole('button',{name:'Bekijk rubric & modelantwoord'}).click();await expect(page.locator('.feedback')).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
 await page.goto('./#/chapter/2');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
 await page.goto('./#/skills');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
});
