   %% Time specifications:
   Fc = 200;                     % hertz
   Fs = 4000;                   % samples per second
   dt = 1/Fs;                   % seconds per sample

   t = (0:dt:2/Fc);     % seconds
   %% Sine wave:
   length(t)
   x = cos(2*pi*Fc*t);
   % Plot the signal versus time:
   figure;
   plot(t,x);
   xlabel('time (in seconds)');
   title('Signal versus Time');
   zoom xon;
   
   csvwrite('toneTime_t.csv',t)
   csvwrite('toneTime_x.csv',x)
   
   L = length(x);
   NFFT = 2^nextpow2(L); % Se calcula la potencia de 2 mayor a L
   espectro = fft(x,NFFT)/L; %se calcula el espectro de la se?al de voz
   f = Fs/2*linspace(0,1,NFFT/2+1); % vector de frecuencias del espectro
   %plot(f,2*abs(espectro(1:NFFT/2+1)))%grafica del espectro unilateral de la se?al
   
   y=2*abs(espectro(1:NFFT/2+1));
   plot(f,y);
   xlabel('Frequencia (Hz) ')
   ylabel('|Y(f)| normal')
   
   csvwrite('toneFrecuency_NFFT.csv',espectro)
   csvwrite('toneFrecuency_espectroDoble.csv',espectro)
   csvwrite('toneFrecuency_y.csv',y)
   csvwrite('toneFrecuency_f.csv',f)
   
   