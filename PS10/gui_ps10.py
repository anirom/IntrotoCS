# -*- coding:utf-8 -*-
# MIT OpenCourseWare
# Word Game

from ps10 import *
import wx
from queue import Queue
from wx.lib.newevent import NewEvent
from threading import Thread

WordSubmission, EVT_WORD_SUBMISSION = NewEvent()

class ModeFrame(wx.Frame):
    """
    Esta clase es el main game mode del menú de selección. Es la primera pantalla que se muestra y es la que se vuelve
    a mostrar después de cada juego.
    """

    def __init__(self):
        """
        Construye la GUI.
        """
        wx.Frame.__init__(self, parent=None, title='Word Game',
                          size=(600, 100),
                          style=wx.DEFAULT_FRAME_STYLE &
                                  ~(wx.RESIZE_BORDER |
                                    wx.MAXIMIZE_BOX |
                                    wx.MINIMIZE_BOX))

        # Crea tres botones lado a lado, cada uno inicia un diferente modo de juego.
        mainPanel = wx.Panel(self, style=wx.TAB_TRAVERSAL)
        options = [('&Solo Game',    self.OnSolo),
                   ('Human vs. &Computer', self.OnVsComp),
                   ('Human vs. &Human',    self.OnVsHuman)]
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        for label, handler in options:
            button = wx.Button(mainPanel, label=label)
            button.Bind(wx.EVT_BUTTON, handler)
            hbox.Add(button, 1, wx.EXPAND | wx.ALL, border=10)
        mainPanel.SetSizer(hbox)
        self.Center()

    def OnSolo(self, event):
        """
        Start a solo game.
        """
        self.Close()
        PlayFrame(HUMAN_SOLO).Show()

    def OnVsComp(self, event):
        """
        Start a vs. computer game.
        """
        self.Close()
        PlayFrame(HUMAN_VS_COMP).Show()

    def OnVsHuman(self, event):
        """
        Start a vs. human game.
        """
        self.Close()
        PlayFrame(HUMAN_VS_HUMAN).Show()

class PlayFrame(wx.Frame):
    """
    La principal ventana de juego
    """
    def __init__(self, mode):
        """
        Construye la GUI
        """
        wx.Frame.__init__(self, parent=None, title='Word Game')
        self.mode = mode
        # Hay cuatro niveles de paneles. El panel externo (outerPanel) que contiene el status bar en la parte baja.
        # Lo demás en la parte superior es statsPanel. Este panel contiene las estadísticas para el Jugador 1 a la
        # izquierda y del Jugador 2 a la derecha. En la parte central, mainPanel contiene una history list de las
        # palabras y el entryPanel debajo de esta. El entryPanel contiene la caja de input y el submit button al lado.

        outerPanel = wx.Panel(self)
        statsPanel = wx.Panel(outerPanel)
        mainPanel = wx.Panel(statsPanel)
        entryPanel = wx.Panel(mainPanel)

        # entryPanel
        self.inputBox = wx.TextCtrl(entryPanel)
        self.submitButton = wx.Button(entryPanel, label='Enter')
        self.submitButton.SetDefault()
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.inputBox, 1, wx.EXPAND)
        hbox.Add(self.submitButton, 0, wx.EXPAND)
        self.submitButton.Bind(wx.EVT_BUTTON, self.OnEnter)
        entryPanel.SetSizer(hbox)

        # mainPanel
        historyLabel = wx.StaticText(mainPanel, label='Palabras previas:')
        self.history = wx.ListBox(mainPanel)
        self.handLabel = wx.StaticText(mainPanel, label='Jugada actual: ')
        inputBoxLabel = wx.StaticText(mainPanel, label='&Ingresa una palabra o "." para terminar el juego:')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(historyLabel, 0, wx.EXPAND)
        vbox.Add(self.history, 1, wx.EXPAND)
        vbox.Add(self.handLabel, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        vbox.Add(inputBoxLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        vbox.Add(entryPanel, 0, wx.EXPAND)
        mainPanel.SetSizer(vbox)

        # statsPanel
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        empty = lambda: wx.StaticText(statsPanel, label='')
        self.stats = [
                wx.StaticText(statsPanel,
                              label='',
                              style=wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE,
                              size=(150, -1))
                for player in [1, 2]]
        hbox.Add(self.stats[0], 0, wx.EXPAND)
        hbox.Add(mainPanel, 1, wx.EXPAND)
        hbox.Add(self.stats[1], 0, wx.EXPAND)
        statsPanel.SetSizer(hbox)

        # outerPanel
        self.statusBar = wx.StatusBar(outerPanel)
        self.statusBar.SetStatusText('Status Bar')
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(statsPanel, 1, wx.EXPAND)
        vbox.Add(self.statusBar, 0, wx.EXPAND)
        outerPanel.SetSizer(vbox)

        # Set some miscellaneous options on the window.
        self.SetMinSize((700, 300))
        self.Center()

        # Bind some event handlers.
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(EVT_WORD_SUBMISSION, self.OnWordSubmission)

        # Start things up.
        self.queue = Queue()
        self.inputBox.SetFocus()
        self.StartGame()

    def OnClose(self, event):
        """
        Maneja el evento en el que la ventana se cierra.
        """
        self.Destroy()
        frame = ModeFrame()
        frame.Show()
        frame.Raise()

    def OnEnter(self, event):
        """
        Maneja el evento en donde submit button es presionado.
        """
        if self.submitButton.IsEnabled():
            self.TryWord(self.inputBox.GetValue())

    def OnWordSubmission(self, event):
        """
        Maneja el evento donde ComputerPlayer ha terminado con una palabra e intenta subirla.
        """
        self.queue.put(self.TryWord(event.word))

    def TryWord(self, word):
        """
        Método común llamado por OnEnter y OnWordSubmission. Este método común en el back-end trata de probar la palabra,
        y después en la ventana despliega si fue exitosa o no.

        returns: Verdadero si el juego aún sigue o Falso si el juego ha terminado.
        """
        try:
            try:
                # Call into the backend.
                points = self.game.tryWord(word)
                if points is not None:
                    # Succeeded, so add the word.
                    self.history.Insert(word, 0)
                    self.statusBar.SetStatusText('Puntos obtenidos: %d puntos.' % points)
                else:
                    # Failed, so just update the status bar.
                    self.statusBar.SetStatusText('No es una palabra valida. Intenta con otra palabra.')
            finally:
                # In any case, clear the inputBox and refresh the stats displays.
                self.inputBox.Clear()
                self.RefreshLabels()
            return True
        except EndHand:
            # We've reached the end of the hand, either voluntarily ('.') or by
            # using up all letters.

            # Summarize the hand.
            if word != '.' and word != '':
                self.history.Insert(word, 0)
            wx.MessageDialog(self,
                    message="El jugador {} ha finalizado el juego.".format(self.game.getCurrentPlayer().getIdNum()),
                    caption="Game Over",
                    style=wx.OK).ShowModal()
            if self.game.nextPlayer():
                # There is another player to switch to.
                self.StartHand()
            else:
                # Game has completely ended.
                if self.game.getNumPlayers() > 1:
                    if self.game.isTie():
                        wx.MessageDialog(self,
                                message="El juego ha terminado en empate.",
                                caption="Game over",
                                style=wx.OK).ShowModal()
                    else:
                        wx.MessageDialog(self,
                                message="Jugador {} ha ganado!".format(self.game.getWinner().getIdNum()),
                                caption="Game over",
                                style=wx.OK).ShowModal()
                self.Close()
            return False

    def RefreshLabels(self):
        """
        Refresh the displays in the stats labels and the hand label.
        """

        self.handLabel.SetLabel("Jugada actual: {}".format(self.game.getCurrentPlayer().getHand()))
        for s, player in zip(self.stats, self.game.players):
            s.SetLabel(str(player))

    def StartGame(self):
        """
        Empieza un juego creando una wordlist y un juego en el backend, después inicializa la jugada.
        """
        wordlist = Wordlist()
        self.game = Game(self.mode, wordlist)
        self.StartHand()

    def StartHand(self):
        """
        Inicia la jugada.
        """
        player = self.game.getCurrentPlayer()
        # Clear the history list box and refresh labels.
        self.history.Clear()
        self.RefreshLabels()
        # Prompt the user so that they can get ready.
        # wx.MessageDialog(self,
        #         message = 'Press OK to begin!',
        #         caption = 'Starting new game',
        #         style = wx.OK).ShowModal()
        if type(player) == ComputerPlayer:
            # Disable controls.
            self.inputBox.Disable()
            self.submitButton.Disable()
            # The way for the worker thread to communicate to the reactor
            # thread is by posting events for the reactor to consume.  The
            # opposite direction is achieved using a synchronized queue.
            def submitWord(word):
                try:
                    wx.PostEvent(self, WordSubmission(word=word))
                    return self.queue.get()
                except:
                    return False

            # Start the computer player in a background thread.
            Thread(target=player.playHand,
                   args=(submitWord, self.game.wordlist)).start()
        else:
            # Enable controls.
            self.inputBox.Enable()
            self.submitButton.Enable()

if __name__ == '__main__':
    app = wx.App()
    frame = ModeFrame()
    frame.Show()
    app.MainLoop()